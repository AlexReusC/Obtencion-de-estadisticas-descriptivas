import csv
import statistics as stats

counter = 0
with open('ulabox_orders_with_categories_partials_2017.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)
    # print(data)

    for i in data:
        counter += 1

    print("#2")
    print("tamaño del dataset: ", counter)

    print("variables observadas")
    variables = list((data)[0].keys())
    # print(variables)

    print("tipos de variables")
    for i in variables:
        print(i, ": discreto")

    print("")
    print("")
    print("")

    print("#3")
    print("maximo y minimo de las variables")

    for i in variables:
        seq = [float(x[i]) for x in data]
        print(i)
        print("min: ", min(seq))
        print("max: ", max(seq))
        print()

    print("")
    print("")
    print("")


    primerCuartil = round((counter + 1) / 4)
    TercerCuartil = round((3 * counter + 3) / 4)

    print("#4")
    print("medidas de tendencia central, dispersion y posicion de las variables")

    for i in variables:
        seq = [float(x[i]) for x in data]
        print(i)
        print("promedio: ", stats.mean(seq))
        print("mediana: ", stats.median_grouped(seq))
        print("moda: ", stats.mode(seq))
        print("desviacion estandar: ", stats.pstdev(seq))
        seq.sort()
        print("primer cuartil: ", seq[primerCuartil], "  TercerCuartil: ", seq[TercerCuartil])
        print("")











#     if(row['sex'] == "male"):
#         male += 1
#     else:
#         female += 1
#
# print(male, female)
