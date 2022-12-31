from translate import Translator
import psycopg2

PGHOST="65.21.248.151"
PGUSER="hamza"
PGDATABASE="cars"
PGPASSWORD="hamza"
PGPORT=5432

offset = 50
conn = psycopg2.connect(
        database=PGDATABASE,
        user = PGUSER,
        password = PGPASSWORD,
        host = PGHOST,
        port = PGPORT
)

cur = conn.cursor()
cur.execute('''select * from en 
            order by car_id ASC
            offset '''+str(offset))

rows = cur.fetchall()
for data in rows:
    print(offset, ": ",data[0])
    languages = [('fr','fr'), ('es','es'), ('ru','ru'), ('de','de'), ('it','it'), ('Greek','gr'), ('tr','tr'), ('ro','ro'), ('fi','fi'), ('swedish','se'), ('no','no'), ('pl','pl')]
    for lang in languages:
        translator = Translator(to_lang=lang[0])
        translation = list(data)
        if translation[2] is not None:  # bodytype
            translation[2] = translator.translate(data[2])
        if translation[7] is not None:  # modification
            translation[7] = translator.translate(data[7])
        if translation[8] is not None:  # powertrainArchitecture
            translation[8] = translator.translate(data[8])
        if translation[10] is not None:  # startofproduction
            translation[10] = translator.translate(data[10])
        if translation[19] is not None:  # dragcoefficient
            translation[19] = translator.translate(data[19])
        if translation[29] is not None:  # engineaspiration
            translation[29] = translator.translate(data[29])
        if translation[32] is not None:  # fuelSystem
            translation[32] = translator.translate(data[32])
        if translation[33] is not None:  # modelEngine
            translation[33] = translator.translate(data[33])
        if translation[36] is not None:  # positionofcylinders
            translation[36] = translator.translate(data[36])
        if translation[39] is not None:  #
            translation[39] = translator.translate(data[39])
        if translation[40] is not None:  # frontbrakes
            translation[40] = translator.translate(data[40])
        if translation[41] is not None:  # frontsuspension
            translation[41] = translator.translate(data[41])
        if translation[43] is not None:  # powersteering
            translation[43] = translator.translate(data[43])
        if translation[44] is not None:  # rearbrakes
            translation[44] = translator.translate(data[44])
        if translation[45] is not None:  # rearsuspension
            translation[45] = translator.translate(data[45])
        if translation[46] is not None:  # steeringtype
            translation[46] = translator.translate(data[46])
        if translation[60] is not None:  # enginelocationnumber1
            translation[60] = translator.translate(data[60])
        if translation[62] is not None:  # enginelocationnumber2
            translation[62] = translator.translate(data[62])
        query = """
        INSERT INTO """+lang[1]+"""(
        car_id, bodytype, brand, doors, endofproduction, generation, model, modification, "powertrainArchitecture", seats, startofproduction, acceleration100, acceleration60, acceleration62, "fuelType", "fuelconsumptionCombined", "fuelconsumptionExtraurban", "fuelconsumptionUrban", maximumspeed, dragcoefficient, fronttrack, height, length, minimumturningcircle, "rearTrack", wheelbase, width, compressionratio, "cylinderBore", engineaspiration, enginedisplacement, engineoilcapacity, "fuelSystem", "modelEngine", numberofcylinders, numberofvalvespercylinder, positionofcylinders, power, torque, drivewheel, frontbrakes, frontsuspension, "numberofGears", powersteering, rearbrakes, rearsuspension, steeringtype, tiressize, wheelrimssize, fueltankcapacity, "kerbWeight", maxload, maxweight, hotcar, addedon, batterycapacity, electricrange, averageenergyconsumptionwltp, averageenergyconsumption, electricmotorpowernumber1, enginelocationnumber1, electricmotorpowernumber2, enginelocationnumber2, systempower, systemtorque, frontoverhang, rearoverhang)
        VALUES ("""+str(translation[0])+""", %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        value = (
            str(translation[1]), str(translation[2]), str(translation[3]), str(translation[4]), str(translation[5]),
            str(translation[6]),
            str(translation[7]), str(translation[8]), str(translation[9]), str(translation[10]), str(translation[11]),
            str(translation[12]),
            str(translation[13]), str(translation[14]), str(translation[15]), str(translation[16]),
            str(translation[17]), str(translation[18]),
            str(translation[19]), str(translation[20]), str(translation[21]), str(translation[22]),
            str(translation[23]),
            str(translation[24]), str(translation[25]), str(translation[26]), str(translation[27]),
            str(translation[28]), str(translation[29]),
            str(translation[30]), str(translation[31]), str(translation[32]), str(translation[33]),
            str(translation[34]), str(translation[35]),
            str(translation[36]), str(translation[37]), str(translation[38]), str(translation[39]),
            str(translation[40]), str(translation[41]),
            str(translation[42]), str(translation[43]), str(translation[44]), str(translation[45]),
            str(translation[46]), str(translation[47]),
            str(translation[48]), str(translation[49]), str(translation[50]), str(translation[51]),
            str(translation[52]), str(translation[53]),
            str(translation[54]), str(translation[55]), str(translation[56]), str(translation[57]),
            str(translation[58]), str(translation[59]),
            str(translation[60]), str(translation[61]), str(translation[62]), str(translation[63]),
            str(translation[64]), str(translation[65]),
            str(translation[66]))
        try:
            cur.execute(query, value)
            conn.commit()
        except psycopg2.errors.UniqueViolation:
            conn.rollback()
            print("Already added")


conn.close()
print("done")