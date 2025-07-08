from main import parse_input, add_contact, change_contact, show_phone, show_all


def test_parse_input():
    assert parse_input("add John 12345") == ("add", ["John", "12345"])
    assert parse_input("   phone Alice  ") == ("phone", ["Alice"])
    assert parse_input("") == ("", [])
    assert parse_input("   ") == ("", [])


def test_add_contact():
    contacts = {}
    assert add_contact(["John", "12345"], contacts) == "✅ Contact added."
    assert contacts == {"John": "12345"}
    assert add_contact(["OnlyName"], contacts).startswith("❌")


def test_change_contact():
    contacts = {"John": "12345"}
    assert change_contact(["John", "54321"], contacts) == "🔄 Contact updated."
    assert contacts["John"] == "54321"
    assert change_contact(["Unknown", "000"], contacts) == "❌ Contact not found."
    assert change_contact(["OnlyName"], contacts).startswith("❌")


def test_show_phone():
    contacts = {"Alice": "111"}
    assert show_phone(["Alice"], contacts) == "📞 Alice's phone number is 111"
    assert show_phone(["Bob"], contacts) == "❌ Contact not found."
    assert show_phone([], contacts).startswith("❌")


def test_show_all():
    contacts = {"A": "1", "B": "2"}
    result = show_all(contacts)
    assert "📇 Contact list:" in result
    assert "📌 A: 1" in result
    assert "📌 B: 2" in result

    assert show_all({}) == "📭 No contacts found."


if __name__ == "__main__":
    test_parse_input()
    test_add_contact()
    test_change_contact()
    test_show_phone()
    test_show_all()
    print("✅ All tests passed.")
