int myAtoi(char* s) {
    int i = 0;
    int sing = 1;
    int res = 0;
    while(s[i] == ' ')
        i++;
    if(s[i] == '+' || s[i] == '-')
    {
        if (s[i] == '-')
            sing = sing * -1;
        i++;
    }
    while (s[i] == '0')
        i++;
    while(s[i] >= '0' && s[i] <= '9'){
        if(res >= (int)(res * 10 + (s[i] - '0')))
        {
            if (sing == -1)
                return -2147483648;
            else
                return 2147483647;
        }
        res = res * 10 + (s[i++] - '0');
    }
    return sing * res;
}


int main()
{
	printf("%d", myAtoi("-91283472332"));
}