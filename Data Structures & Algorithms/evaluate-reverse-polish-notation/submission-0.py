from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st: list[int] = []

        for token in tokens:
            match token:
                case "+":
                    b = st.pop()
                    a = st.pop()
                    st.append(a + b)

                case "-":
                    b = st.pop()
                    a = st.pop()
                    st.append(a - b)

                case "*":
                    b = st.pop()
                    a = st.pop()
                    st.append(a * b)

                case "/":
                    b = st.pop()
                    a = st.pop()
                    st.append(int(a / b))

                case _:
                    st.append(int(token))

        return st[-1]