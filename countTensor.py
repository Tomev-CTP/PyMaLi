import numpy as np

def countTensor(vectors, tensor=[]):
    ## ASSIGNING TERMINATION CONDITION AT THE BEGINNING
    # Check if single vector was passed
    if len(vectors) == 1:
        # Insert it's elements into target if so and return
        for el in vectors[0]:
            tensor.append(el)
        return tensor

    # If there are more than one vectors For each vector take first vector out of the list
    vec = vectors.pop(0)

    # For each element in this vector
    for el in vec:
        # IMPORTANT
        # Copy before each recurrence call
        vs = vectors.copy()
        # Add this vectors i-th element list
        tensor.append([])
        ## RECURRENCE CALL
        # Call this method on reduced data set
        countTensor(vs, tensor[-1])
        # Multiply each obtained element by element from vector vec
        # Side note: I believe this could be performed in a more tricky way by putting el inside newly created list
        # I will provide test it in another method.
        # CAUTION -- following method is also use recurrence
        multiplyEachElement(tensor[-1], el)

    # Return the tensor
    return tensor


def multiplyEachElement(tensor, multiplier=1):
    ## ASSIGNING TERMINATION CONDITION AT THE BEGINNING
    # IF tensor is empty just return (I believe this should not happen)
    if len(tensor) == 0:
        return

    # Check if first element is a list. If not, then just multiply elements
    if not isinstance(tensor[0], list):
        for i in range(len(tensor)):
            #tensor[i] *= multiplier
            tensor[i] = np.kron(multiplier, tensor[i])
        return

    # Otherwise call multiplying function for each element (list) of tensor
    for l in tensor:
        multiplyEachElement(l, multiplier)


def countTensorTrickly(vectors, tensor=[1]):
    ## ASSIGNING TERMINATION CONDITION AT THE BEGINNING
    # Check if single vector was passed
    # CAUTION: Note how tensor is initiated. That's the whole trick of the method.
    # Compare with multiply each element approach in CountTensor

    if len(vectors) == 1:
        multiplier = tensor[0]
        tensor.clear()
        # Insert it's elements into target if so and return
        for el in vectors[0]:
            tensor.append(np.kron(multiplier,el))
        return tensor

    # If we're not multiplying information about multiplier should be deleted
    tensor.clear()

    # If there are more than one vectors For each vector take first vector out of the list
    vec = vectors.pop(0)

    # For each element in this vector
    for el in vec:
        # IMPORTANT
        # Copy before each recurrence call
        vs = vectors.copy()
        # Add this vectors i-th element list
        tensor.append([el])
        ## RECURRENCE CALL
        # Call this method on reduced data set
        countTensorTrickly(vs, tensor[-1])


    # Return the tensor
    return tensor




######### TESTS #############
sigma_z=np.array([[1,0],[0,-1]])
'''
print(countTensorTrickly([
    [1*sigma_z,2*sigma_z],
    [2*np.eye(4),3*np.eye(4),4*np.eye(4),5*np.eye(5)],
    [10*sigma_z,1000*sigma_z,10e6*sigma_z]
]))
'''

print(countTensor([
    [1*sigma_z,2*sigma_z],
    [2*np.eye(4),3*np.eye(4),4*np.eye(4),5*np.eye(5)],
    [10*sigma_z,1000*sigma_z,10e6*sigma_z]
]))


#print(np.kron(sigma_z,np.eye(2)))
