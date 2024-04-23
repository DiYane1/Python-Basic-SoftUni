def calculate_digit_sum(number):
    return sum(int(digit) for digit in str(number))


def main():
    sequence = input().split()
    text = input().strip()

    message = []

    for num in sequence:
        index = calculate_digit_sum(num)
        if index > len(text):
            index %= len(text)

        char = text[index]
        message.append(char)
        text = text[:index] + text[index + 1:]

    result = ''.join(message)
    print(result)


if __name__ == "__main__":
    main()
