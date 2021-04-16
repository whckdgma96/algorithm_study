def solution(genres, plays):
    genre_total_play_dic = {}
    genre_index_play_array_dic = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genre_total_play_dic:
            genre_total_play_dic[genre] = play
            genre_index_play_array_dic[genre] = [[i, play]]
        else:
            genre_total_play_dic[genre] += play
            genre_index_play_array_dic[genre].append([i, play])
    sorted_genre_play_array = sorted(genre_total_play_dic.items(), key=lambda item: item[1], reverse=True)
    result = []
    for genre, value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dic[genre]
        sorted_index_play_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        for i in range(len(sorted_index_play_array)):
            if i > 1:
                break
            result.append(sorted_index_play_array[i][0])

    return result