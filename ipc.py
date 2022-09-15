from multiprocessing import shared_memory

if __name__ == "__main__":
    shm_a = shared_memory.SharedMemory(name="myshm", create=False)
    buffer = shm_a.buf
    print(buffer[0])
