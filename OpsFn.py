# The program computes the operations +,-,*,/
# Given the list of such computations, it outputs the results in a list

def generate_qns_from_list(input_list):

    output_list = []
    count = 0
    for item in input_list:
        count = count+1
        length = len(item)
        sign = item[0]
        print(item)
        if(sign == "+"):
            result = item[1]+item[2]
        elif(sign == "-"):
            result = item[1]-item[2]
        elif(sign == "x"):
            result = item[1]*item[2]
        else:
            result = item[1]/item[2]
        val = 3
        while(val < length):
            if(sign == "+"):
                result = result+item[val]
            elif(sign == "-"):
                result = result-item[val]
            elif(sign == "x"):
                result = result*item[val]
            else:
                result = result/item[val]
            val = val+1
        output_list.append(result)
        return output_list


input_list1 = [["+", 1, 2, 3],
               ["-", 2, 4, 1],
               ["x", 2, 3, 4],
               ["+", 1, 2, 3, 4],
               ["/", 6, 3]]
output_list = generate_qns_from_list(input_list1)
print(output_list)
input_list2 = [["+", 5, 25, 40, 67, 74], ["*", 35, 25, 70]]
output_list2 = generate_qns_from_list(input_list2)
print(output_list2)
