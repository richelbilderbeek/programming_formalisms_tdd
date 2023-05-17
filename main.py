import my_functions

if __name__ == "__main__":
    sequence_1 = "GCATGCG"
    sequence_2 = "GATTACA"
    print("Brute-force:")
    my_functions.print_alignment(sequence_1, sequence_2, my_functions.align_bf(sequence_1, sequence_2))
    print("needleman_wunsch:")
    my_functions.print_alignment(sequence_1, sequence_2, my_functions.align_fast(sequence_1, sequence_2))
    