import pygame, sys
import text
#Function to fill the matrix
def edit_distance(s1,s2):
    matrix = {}
    len_s1 = len(s1)
    len_s2 = len(s2)
    for i in range(len_s2+1):
        matrix[i, 0] = i
    for j in range (len_s1+1):
        matrix[0, j] = j
    for j in range(1,len_s1):
        for i in range(1,len_s2):
            if s1[j] == s2[i]:
				#print ("Equal now:"+s1[j-1]+ "=" + s2[i-1])
				matrix[i, j] = matrix[i-1, j-1] 
            else:
				matrix[i, j] = min(matrix[i-1, j] + 1, matrix[i, j-1] + 1, matrix[i-1, j-1] + 1) 
    return matrix

#Function to get the successors of a node

def graph(node, matrix, l1, l2):
	successors = []
	if node[0] == len(l2):
		if node[1] == len(l1):
			return successors
		if matrix[ node[0], node[1]+1 ] > matrix[ node[0], node[1] ]:
			successors.append( [node[0], node[1]+1] )
		return successors
	elif node[1] == len(l1):
		if matrix[ node[0]+1, node[1] ] > matrix[ node[0], node[1] ]:
			successors.append( [node[0]+1, node[1]] )
		return successors
	else:
		if matrix[ node[0]+1, node[1] ] > matrix[ node[0], node[1] ]:
			successors.append( [node[0]+1, node[1]] )	
		if matrix[ node[0], node[1]+1 ] > matrix[ node[0], node[1] ]:
			successors.append( [node[0], node[1]+1] )
		if matrix[ node[0] + 1, node[1] + 1 ] > matrix[ node[0], node[1] ]:
			successors.append( [node[0]+1, node[1]+1] )
		if matrix[ node[0] + 1, node[1] + 1 ] == matrix[ node[0], node[1] ] and l2[node[0]] == l1[node[1]]:
			successors.append( [node[0]+1, node[1]+1] )
		return successors 

#Function to do a DFS on the matrix and get all optimal edit  sequences
def all_paths(matrix, start, end, l1, l2, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in graph(start, matrix, l1, l2):
            if node not in path:
                paths += all_paths(matrix, node, end, l1, l2, path)
        return paths


def begin(): 
	graphics_result = []
	matrix = {}
	result = []
	s1,s2=text.tri()
	l1 = len(s1)
	l2 = len(s2)
	matrix = edit_distance(' '+s1,' '+s2)
	start = [0,0]
	end = [len(s2),len(s1)]
	result = all_paths(matrix, start, end, s1, s2)
	count = 0
	graphics_result.append(matrix)
	graphics_result.append(s1)
	graphics_result.append(s2)
	graphics_result.append(result)
	return graphics_result
