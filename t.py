# Frontend: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33 dst  kelipatan 3
# Backend: 5, 10, 15, 20  kelipatan 5
# Frontend Backend: 15, 30, 45  kelipatan 15



def test(n: int) -> str:
    result = ""
    for i in range(1, n + 1):
        if i % 15 == 0:
            result += "Frontend Backend" 
        elif i % 3 == 0:
            result += "Frontend"
        elif i % 5 == 0:
            result += "Backend"

        else:
            result += f"{str(i)}"
        
        if i != n:
            result += ","
    
    return result


print(test(50))
