from server.misc.utils import flatten
i = [(True, [{'imgSrc': '/data/product/img_s1_37170'}, {'imgSrc': '/data/product/img_s1_37171'}, {'imgSrc': '/data/product/img_s1_37172'}, {'imgSrc': '/data/product/img_s1_37173'}, {'imgSrc': '/data/product/img_s1_37174'}, {'imgSrc': '/data/product/img_s1_37175'}, {'imgSrc': '/data/product/img_s1_37176'}, {'imgSrc': '/data/product/img_s1_37177'}, {'imgSrc': '/data/product/img_s1_39928'}, {'imgSrc': '/data/product/img_s1_39929'}, {'imgSrc': '/data/product/img_s1_39930'}, {'imgSrc': '/data/product/img_s1_39931'}, {'imgSrc': '/data/product/img_s1_39932'}, {'imgSrc': '/data/product/img_s1_39933'}, {'imgSrc': '/data/product/img_s1_39934'}, {'imgSrc': '/data/product/img_s1_44519'}, {'imgSrc': '/data/product/img_s1_44520'}, {'imgSrc': '/data/product/img_s1_44521'}, {'imgSrc': '/data/product/img_s1_20266'}, {'imgSrc': '/data/product/img_s1_20267'}, {'imgSrc': '/data/product/img_s1_20268'}, {'imgSrc': '/data/product/img_s1_20269'}, {'imgSrc': '/data/product/img_s1_20270'}, {'imgSrc': '/data/product/img_s1_28038'}, {'imgSrc': '/data/product/img_s1_28039'}, {'imgSrc': '/data/product/img_s1_15534'}, {'imgSrc': '/data/product/img_s1_15527'}, {'imgSrc': '/data/product/img_s1_15536'}, {'imgSrc': '/data/product/img_s1_15530'}, {'imgSrc': '/data/product/img_s1_15529'}, {'imgSrc': '/data/product/img_s1_15535'}, {'imgSrc': '/data/product/img_s1_15531'}, {'imgSrc': '/data/product/img_s1_15532'}, {'imgSrc': '/data/product/img_s1_15526'}, {'imgSrc': '/data/product/img_s1_15533'}, {'imgSrc': '/data/product/img_s1_37622'}, {'imgSrc': '/data/product/img_s1_4463'}, {'imgSrc': '/data/product/img_s1_4466'}, {'imgSrc': '/data/product/img_s1_30931'}, {'imgSrc': '/data/product/img_s1_4464'}, {'imgSrc': '/data/product/img_s1_4467'}, {'imgSrc': '/data/product/img_s1_46519'}, {'imgSrc': '/data/product/img_s1_46520'}, {'imgSrc': '/data/product/img_s1_4465'}, {'imgSrc': '/data/product/img_s1_46287'}, {'imgSrc': '/data/product/img_s1_46288'}, {'imgSrc': '/data/product/img_s1_46289'}, {'imgSrc': '/data/product/img_s1_46290'}, {'imgSrc': '/data/product/img_s1_46291'}, {'imgSrc': '/data/product/img_s1_46550'}, {'imgSrc': '/data/product/img_s1_46551'}, {'imgSrc': '/data/product/img_s1_46552'}, {'imgSrc': '/data/product/img_s1_46553'}, {'imgSrc': '/data/product/img_s1_5973'}, {'imgSrc': '/data/product/img_s1_5971'}, {'imgSrc': '/data/product/img_s1_5974'}, {'imgSrc': '/data/product/img_s1_5972'}, {'imgSrc': '/data/product/img_s1_5970'}, {'imgSrc': '/data/product/img_s1_5975'}, {'imgSrc': '/data/product/img_s1_5976'}, {'imgSrc': '/data/product/img_s1_19327'}, {'imgSrc': '/data/product/img_s1_19328'}, {'imgSrc': '/data/product/img_s1_19326'}, {'imgSrc': '/data/product/img_s1_19332'}, {'imgSrc': '/data/product/img_s1_19329'}, {'imgSrc': '/data/product/img_s1_19330'}, {'imgSrc': '/data/product/img_s1_19331'}])]

i = [e[1] for e in i if e[0]]
# print(i)
print(list(flatten(i, ignore_types=(str, bytes, dict))))