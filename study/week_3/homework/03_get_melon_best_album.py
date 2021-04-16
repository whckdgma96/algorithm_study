genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    all_genre_dict = {}
    nth_genre_play_dict = {}
    n = len(genre_array)
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in all_genre_dict:
            all_genre_dict[genre] = play
            nth_genre_play_dict[genre] = [[i,play]]
        else:
            all_genre_dict[genre] += play
            nth_genre_play_dict[genre].append([i,play])
    print(all_genre_dict)
    print(nth_genre_play_dict)
    print("==============================================================================")
    result = []
    sorted_all_genre_dict = sorted(all_genre_dict.items(), key = lambda item:item[1], reverse=True)
    print(sorted_all_genre_dict)
    for genre, value in sorted_all_genre_dict:
        nth_play_array = nth_genre_play_dict[genre]
        sorted_nth_play_array = sorted(nth_play_array, key=lambda item:item[1], reverse=True)
        print(sorted_nth_play_array)

        for i in range(len(sorted_nth_play_array)):
            if i < 2:
                result.append(sorted_nth_play_array[i][0])
            else:
                break



    return result







print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!