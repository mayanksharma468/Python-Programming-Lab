def shutdown(sd):
    if sd=='Yes':
        return 'Shutting down'
    elif sd=='No':
        return 'Shutdown aborted'
    else:
        return 'Sorry'
sd=input('enter command: ')
print(shutdown(sd))
