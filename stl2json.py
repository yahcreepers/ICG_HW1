from this import d
import numpy as np
import json
from stl import mesh
my_mesh = mesh.Mesh.from_file( "yourMesh.stl" )
print( my_mesh )
print( type( my_mesh.data ) )
print( len( my_mesh.data ) )
dic = dict({})
# count = 0
for i in my_mesh.data:
    # if count > 10 : break
    # count += 1
    # print( my_mesh.data[i] )
    # print( np.linalg.norm( my_mesh.data[i][0] ) )
    l = np.linalg.norm( i[0] )
    nor_vec = i[0] / l
    for j in i[1]:
        vtx = str(j)
        if vtx in dic:
            dic[vtx] += nor_vec
        else:
            dic[vtx] = nor_vec      
print( "build dic" )  
for k, v in dic.items() :
     dic[k] = v / np.linalg.norm( v )
    #  print( k, " : ", dic[k] )
print( "norm dic" )
# print( len( dic ) )
outp_dic = { "vertexPositions" : [], "vertexNormals" : [], "vertexFrontcolors" : [] }
# count = 0
for i in my_mesh.data:
    # if count > 10 : break
    # count += 1
    for j in i[1]:
        outp_dic["vertexPositions"].extend(list( map( float, j ) ) )
        outp_dic["vertexNormals"].extend( list( map( float, dic[str( j )] ) ) )
        outp_dic["vertexFrontcolors"].extend( [ 1.0, 1.0, 1.0 ] )
file = open("./model/Kirby.json", "w")
json.dump(outp_dic, file)
