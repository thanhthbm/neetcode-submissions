class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st: list[int] = []

        for x in asteroids:
            if x > 0:
                st.append(x)
                continue

            while st and st[-1] > 0:
                if st[-1] + x < 0:
                    st.pop()
                elif st[-1] + x == 0:
                    st.pop()
                    x = 0
                    break
                else:
                    x = 0
                    break

            if x:
                st.append(x)

        return st