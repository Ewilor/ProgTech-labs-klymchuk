import grades_management as gm

data ={ ('8-A','Soroka I.I.'):{'Math':[12, 10, 8, 9],
                         'Ukr literature':[9, 7],
                         'Chemistry':[6, 8, 7],
                         'Physics':[11, 12, 11, 12],
                         'PE':[10, 10, 10, 10]
                         },
        ('8-A','Nikson A.V.'):{'Math':[12, 11, 10, 7],
                         'Ukr literature':[10, 11],
                         'Chemistry':[9, 8, 10],
                         'Physics':[10, 10, 7, 6],
                         'PE':[7, 8, 9, 10]
                         },
    #    ('5-C','Kozak A.S.'):{'Math':[9, 10, 10, 10],
    #                      'Ukr literature':[9, 10],
    #                      'History':[6, 10, 11, 8],
    #                      'English':[5, 12, 10, 11],
    #                      'PE':[9, 8, 6, 4]
    #                      },
    #    ('5-B','Moliga T.P.'):{'Math':[11, 11, 11, 10],
    #                      'Ukr literature':[12, 10, 11],
    #                      'History':[10, 10, 11, 12],
    #                      'English':[11, 10, 12, 10, 11],
    #                      'PE':[10, 10, 10, 10]
    #                      },
    #    ('5-C','Vinnichenko D.R.'):{'Math':[10, 10, 10, 10],
    #                      'Ukr literature':[11, 10],
    #                      'History':[9, 10, 11, 12],
    #                      'English':[11, 12, 7, 9, 10],
    #                      'PE':[5, 5, 8, 9]
    #                      }
}


gm.add_child(data, ('8-C','Melnyk D.R.'))
