# main.py
## Selector
import evaluator
import piecewise_builder
import step_graph

def menu():
    print("\n=== Unit Step Function Project ===")
    print("1. Evaluator (compute u(t-a))")
    print("2. Piecewise Builder")
    print("3. Graph Creator (via matplotlib)")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Select an option (1, 2, 3): ").strip()

        if choice == "1":
            evaluator.main()

        elif choice == "2":
            piecewise_builder.main()

        elif choice == "3":
            step_graph.main()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 0.")

if __name__ == "__main__":
    main()
