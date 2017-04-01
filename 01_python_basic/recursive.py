times = int(input("how many times do you want to curse the beat?"))
def recurse_beast(a):
    if a == 0:
        print("curse complete")
    else:
        print("Fusion!! (%d times left)" % (a-1))
        recurse_beast(a-1)

recurse_beast(times)
