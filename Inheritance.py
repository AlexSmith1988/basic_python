class Test:
    pass


test = Test()
test.maan = 42
test.__setattr__("check", 10)
print(f"{test.maan}")
