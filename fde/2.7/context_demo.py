class Timer:
    def __enter__(self):
        print("start")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("end")


with Timer():
    print("working")
