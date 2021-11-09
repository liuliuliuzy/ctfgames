unsigned __int64 play_maze()
{
    int starti;           // er14
    int v1;               // eax
    __int64 nowj;         // r12
    __int64 nowi;         // rbx
    __int64 v4;           // rbp
    char *v5;             // r13
    int v6;               // eax
    char v7;              // bp
    char *v9;             // [rsp+0h] [rbp-C868h]
    unsigned int startj;  // [rsp+Ch] [rbp-C85Ch]
    int v11;              // [rsp+1Ch] [rbp-C84Ch]
    char s[51208];        // [rsp+20h] [rbp-C848h] BYREF
    unsigned __int64 v13; // [rsp+C828h] [rbp-40h]

    v13 = __readfsqword(0x28u);
    memset(s, 0, 0xC800uLL);
    starti = rand() % 40;
    v1 = rand();
    nowj = v1 % 40;
    startj = v1 % 40;
    v11 = rand() % 40;
    nowi = starti;
    v9 = &s[1280 * v11 + 32 * (rand() % 40)];
    generate_maze(s);
    while (1)
    {
        v4 = 32 * (nowj + 40 * nowi);
        v5 = &s[v4];
        if (&s[v4] == v9)
            break;
        puts("This room has exits to the ");
        v6 = *(_DWORD *)&s[v4 + 28];
        if ((v6 & 8) != 0)
        {
            puts("North");
            v6 = *(_DWORD *)&s[v4 + 28];
        }
        if ((v6 & 4) != 0)
        {
            puts("East");
            v6 = *(_DWORD *)&s[1280 * nowi + 28 + 32 * nowj];
        }
        if ((v6 & 2) != 0)
        {
            puts("South");
            v6 = *(_DWORD *)&s[1280 * nowi + 28 + 32 * nowj];
        }
        if ((v6 & 1) != 0)
            puts("West");
        if (s[1280 * nowi + 32 * nowj])
            printf("On the wall is written: %s\n", &s[v4]);
        printf(
            "\n"
            "What would you like to do? (w - go north, a - go west, s - go south, d - go east, x - write something, m - show map): ");
        v7 = fgetc(stdin);
        if (v7 == 10)
        {
        LABEL_28:
            puts("I'm not sure I understand.");
        }
        else
        {
            while (fgetc(stdin) != 10)
                ;
            switch (v7)
            {
            case 'a':
                if ((s[1280 * nowi + 28 + 32 * nowj] & 1) == 0)
                    goto LABEL_26;
                nowj = (int)--startj;
                break;
            case 'd':
                if ((s[1280 * nowi + 28 + 32 * nowj] & 4) == 0)
                    goto LABEL_26;
                nowj = (int)++startj;
                break;
            case 'm':
                print_maze(s, (unsigned int)starti, startj);
                continue;
            case 's':
                if ((s[1280 * nowi + 28 + 32 * nowj] & 2) == 0)
                    goto LABEL_26;
                nowi = ++starti;
                break;
            case 'w':
                if ((s[1280 * nowi + 28 + 32 * nowj] & 8) != 0)
                    nowi = --starti;
                else
                LABEL_26:
                    puts("There's a wall there.");
                break;
            case 'x':
                puts(
                    "Your magnificently magestic magic marker magically manifests itself in your hand. What would you like to write?");
                fgets(v5, 33, stdin);
                break;
            default:
                goto LABEL_28;
            }
        }
    }
    puts("You were eaten by a Grue.");
    return __readfsqword(0x28u) ^ v13;
}