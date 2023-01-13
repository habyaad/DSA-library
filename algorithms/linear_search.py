class Search:
    def __init__(self) -> None:
        pass
    def search(self, num_list, num)->int:
        for i in range(len(num_list)):
            if num_list[i] == num:
                return i
            else:
                return None
if __name__ == "__main__":
    unsorted_list = [2,3,5,6,7,9, 1,4]
    searchAlg = Search()
    index = searchAlg.search(unsorted_list, 0)
    print(index)