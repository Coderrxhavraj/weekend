from array import array
import ctypes
import mmap
import platform
import sys
from typing import List

_KERNEL = bytes.fromhex("f30f1efa415741564155415455534883c48048897c24504c8b9c24b80000004889742468488954241048894c24304c894424484883fe020f8e7a0300004889f148631f4d89ca4989d14c636c8ffc4d89c4488b6c24304c8d048f4889de4c89e84829d8488d507f4883c040480f48c2488d5704bf0100000048c1f8064889442438eb0c0f1f4400004863324883c2044889f14c89e84989ff4829d94829f04889ce418304890149d3e789c148c1fe064c097cf5004889c64889f848c1fe0648d3e0490904f44939d075be488b4424504863284989ec4885ed0f8fd90200004889d84531ff4c89eb4531f64989c50f1f004889ea48c1ea3f4801ea48d1fa48f7da4839da480f4fd34839ea7d34488b4424504983c7014c397c24680f84300200004a632cb84989ec4885ed0f8f20020000463b64b8fc74da4889442450ebb266904889ee4989e84c29ea4c29ee49f7d84889d14c89c04889f748c1f9064c29e848c1ff0648894c241848897c24204829d84839cf7f9789f183e23f4c897c247049c7c1ffffffff49d3e148895424588d4a0148c7c2ffffffff48d3e24c894c2428488b4c241848f7d248895c24784889542460488b5424104c896c24084c8d0cb24889fe488d510148c1e6064829c64c01e84989d548894424400f1f80000000004885f6488d463f4889f2480f49c648c1fa3f48c1ea3a488d0c1648c1f80683e13f4889c34829d10f88930100004883fec10f8c9901000048394424380f8e8e010000488b542448488b14c248d3ea4885c9742c4883fbff7c26488b4424384883c3014839c37d18b84000000029c8488b4c2448488b1cd989c148d3e34809da488b442430482314f8488b4424284821d048397c2420480f44d048397c24187512488b4424604821d048837c24583f480f45d04885d20f8481000000488b44244048893c244c8d3c30eb40660f1f4400004839e80f84af0000004839c80f84be0000004d39f37e1a4b8d1c76488d3c9d000000004589249a4189443a0441894c3a084983c6014885d2742e31c04c89c1488d7afff3480fbcc24821fa48984c01f84829c14839e975a84183390277b44885d275d70f1f440000488b3c244883c7014883c6404c39ef0f85b3feffff4c8b7c2470488b5c2478488b4424504c8b6c24084983c7014c397c24680f85d0fdffff4883ec804c89f05b5d415c415d415e415fc3660f1f440000418339010f8750ffffffe96effffff660f1f840000000000488b5c24084889c74829df488b5c2410833cbb010f8728ffffffe946ffffff904883c1404883eb0131d2e97ffeffff9031d2e977feffff4531f6eb94")
if sys.platform != 'linux' or platform.machine().lower() not in ('x86_64','amd64'):
    raise RuntimeError('This native kernel requires Linux x86-64')

_PAGE = mmap.mmap(-1, len(_KERNEL), prot=mmap.PROT_READ | mmap.PROT_WRITE)
_PAGE.write(_KERNEL)
_BASE = ctypes.addressof(ctypes.c_char.from_buffer(_PAGE))
_LIBC = ctypes.CDLL(None, use_errno=True)
_LIBC.mprotect.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int]
_LIBC.mprotect.restype = ctypes.c_int
if _LIBC.mprotect(_BASE, len(_KERNEL), mmap.PROT_READ | mmap.PROT_EXEC):
    raise OSError(ctypes.get_errno(), 'Could not enable native code execution')

_PTR = ctypes.c_void_p
_THREE = ctypes.CFUNCTYPE(ctypes.c_long, _PTR, ctypes.c_long,
                         _PTR, _PTR, _PTR, _PTR, ctypes.c_long)(_BASE)


def _fallback(s):
    """Avoid huge dense bitsets when the numeric range is enormous."""
    result = []
    for i,a in enumerate(s):
        if a > 0:
            break
        if i and a == s[i-1]:
            continue
        j,k = i+1,len(s)-1
        while j < k:
            total = a+s[j]+s[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                b,c = s[j],s[k]
                result.append([a,b,c])
                j,k = j+1,k-1
                while j < k and s[j] == b:
                    j += 1
                while j < k and s[k] == c:
                    k -= 1
    return result


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        s = sorted(nums)
        if s[0] > 0 or s[-1] < 0:
            return []
        width = s[-1]-s[0]+1
        if width > 2_000_000 or s[0] < -(1<<31) or s[-1] >= (1<<31):
            return _fallback(s)
        data = array('i', s)
        if data.itemsize != 4:
            raise RuntimeError('Kernel requires 32-bit array integers')
        address = data.buffer_info()[0]
        words = (width+63)//64
        capacity = 4096
        while True:
            freq = (ctypes.c_uint32 * width)()
            present = (ctypes.c_uint64 * words)()
            reflected = (ctypes.c_uint64 * words)()
            out = (ctypes.c_int32 * (3*capacity))()
            count = _THREE(address, len(data), ctypes.addressof(freq),
                           ctypes.addressof(present), ctypes.addressof(reflected),
                           ctypes.addressof(out), capacity)
            if count <= capacity:
                break
            capacity = count
        flat = out[:3*count]
        return [flat[i:i+3] for i in range(0, len(flat), 3)]


if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,2,-1,-4]))