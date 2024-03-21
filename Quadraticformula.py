import streamlit as st

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        real_part = -b / (2*a)
        imaginary_part = (-discriminant)**0.5 / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

def main():
    st.title("Quadratic Equation Solver")

    st.write("Enter the coefficients of the quadratic equation ax^2 + bx + c = 0")
    a = st.number_input("Enter the value of a", value=1.0)
    b = st.number_input("Enter the value of b", value=0.0)
    c = st.number_input("Enter the value of c", value=0.0)

    if st.button("Calculate Roots"):
        root1, root2 = quadratic_roots(a, b, c)
        st.success(f"The roots of the quadratic equation are: {root1} and {root2}")

if __name__ == "__main__":
    main()
