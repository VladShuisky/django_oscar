# def get_queryset(self):
#     year_list = self.request.GET.getlist('year')
#     genres_list = self.request.GET.getlist('genres')
#     print(year_list, genres_list)
#     if year_list and genres_list:
#         queryset = Movie.objects.filter(
#             year__in=year_list, genres__in=genres_list
#         )
#         return queryset
#     elif genres_list == False:
#         queryset = Movie.objects.filter(year__in=year_list)
#         return queryset
#     elif year_list == False:
#         queryset = Movie.objects.filter(genres__in=genres_list)
#         return queryset
#     else:
#         pass
#
# # if year_list and genres_list == False:
# #     queryset = Movie.objects.filter(year__in=year_list)
# #     return queryset
# # elif genres_list and year_list == False:
# #     queryset = Movie.objects.filter(genres__in=genres_list)
# #     return queryset
# # else
#
#
#         if year_list==True and genres_list == False:
#             print('пошел по ветке где нет жанра')
#             queryset = Movie.objects.filter(year__in=year_list)
#             return queryset
#         elif genres_list==True and year_list == False:
#             print('Пошел по ветке где нет года')
#             queryset = Movie.objects.filter(genres__in=genres_list)
#             return queryset
#         elif genres_list and year_list:
#             print('пошел по 3 ветке')
#             queryset = Movie.objects.filter(year__in=year_list, genres__in=genres_list)
#             return queryset
#         else:
#             print('по 4 ветке')
#             queryset = Movie.objects.filter(year__in=year_list, genres__in=genres_list)
#             return queryset