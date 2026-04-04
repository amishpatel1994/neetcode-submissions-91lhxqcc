class Solution:

    def encode(self, strs: List[str]) -> str:
        # <length>,<length_str_1>,<length_str_n>,<strs>
        str_lens = [str(len(strs))] + [str(len(s)) for s in strs]
        return "á".join(str_lens) + "á" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        elems = s.split("á")
        length = int(elems[0])
        res = []
        strs_str = elems[-1]
        for i in range(1, length+1):
            str_len = int(elems[i])
            res.append(strs_str[:str_len])
            strs_str = strs_str[str_len:]
        return res
