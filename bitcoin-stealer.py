agreed = input("do you agree to get robbed? (Y/N): ").upper()

if agreed in ["Y", "YE", "YES"]:
    print("Okay give us your money (:")
elif agreed in ["N", "NO"]:
    print("aww ):")
else:
    print("idc, i will rob you anyway.")
