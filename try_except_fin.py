#try_except_fin.py

def main():
    try:
        1/0
        # 1/1
    except:
        print('Exception')
    else:
        print('Else')
    finally:
        print('finally')

        
    pass




if __name__ == '__main__':
    main()
    
