#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-

# Imports
import os, sys, re, errno

# I always check and avoid Python 2.x
if not sys.version_info[0] == 3:
    print("CRITICAL ERROR. You are using Python 2.x and I only run with Python 3")
    exit(1)

# Directorios de trabajo
dirIn="."
dirOut="out"

# Compile the regex... 
#regexPrimario = re.compile(r'(?P<pre>(.*)) (!\[|\[)(?P<com1>(.*))\]\((?P<url1>(.*))\)(?P<post>(.*))')
regexPrimario = re.compile(r'(?:(?P<pre>(.*)) )?(!\[|\[)(?P<com1>(.*))\]\((?P<url1>(.*))\)(?P<post>(.*))')
regexSecundario = re.compile(r'!\[(?P<com1>(.*))\]\((?P<url1>(.*))\)')
regexEtiqueta = re.compile(r'\"(?P<etiqueta>(.*))\"')

# Creo el directorio de salida
try:
    os.makedirs(dirOut)
except OSError as e:
    if e.errno != errno.EEXIST:
            raise

for filename in os.listdir(dirIn):

    # Analizo los Markdown's
    if filename.endswith(".md"): 

        # Preparo el nombre completo
        pathFilenameIn=os.path.join(dirIn, filename)
        pathFilenameOut=os.path.join(dirOut, filename)
        #print(pathFilenameIn)
        print(pathFilenameOut)

        # Read el fichero
        with open(pathFilenameIn, 'r', encoding='utf-8') as fdIn:
            filedata = fdIn.read()

            # Quickly replace some anoying items
            filedata = filedata.replace('\[', '[')
            filedata = filedata.replace('\]', ']')
            filedata = filedata.replace('\_', '_')
            filedata = filedata.replace('\*', '*')
            filedata = filedata.replace('\#', '#')
            filedata = filedata.replace('\\\\', '\\')

            # Pass the whole filedata into a list of strings
            lines = filedata.splitlines()
            newLines = []

            # Iteración 
            frontMatter=False
            fmCategories=False
            fmTags=False
            for index, line in enumerate(lines):
                # Detecto el Front Matter
                if ( index == 0 ) and line == "---": 
                    frontMatter=True
                if frontMatter == True and ( index != 0 ) and line == "---": 
                    frontMatter=False
                    fmCategories=False
                    fmTags=False
                    if len(catLine) != 0:
                        newLines.append(catLine)
                    if len(tagLine) != 0:
                        newLines.append(tagLine)
                    newLines.append("excerpt_separator: <!--more-->")
                if frontMatter == True and line.startswith("categories:"): 
                    catLine=""
                    fmCategories=True
                    fmTags=False
                if frontMatter == True and line.startswith("tags:"): 
                    tagLine=""
                    fmCategories=False 
                    fmTags=True

                if fmCategories == True or fmTags == True: 
                    if fmCategories == True: 
                        if line.startswith("categories:"): 
                            catLine="categories:"
                        else:
                            matchEtiqueta = re.search(regexEtiqueta, line)
                            if ( matchEtiqueta ):
                                if matchEtiqueta.group('etiqueta') is not None:
                                    etiqueta=matchEtiqueta.group('etiqueta')
                                    catLine = f'{catLine:s} {etiqueta:s}'
                    if fmTags == True: 
                        if line.startswith("tags:"): 
                            tagLine="tags:"
                        else:
                            matchEtiqueta = re.search(regexEtiqueta, line)
                            if ( matchEtiqueta ):
                                if matchEtiqueta.group('etiqueta') is not None:
                                    etiqueta=matchEtiqueta.group('etiqueta')
                                    tagLine = f'{tagLine:s} {etiqueta:s}'
                else:
                    newLines.append(line)


            # Fully convert the whole filedata into a list of strings
            #lines = filedata.splitlines()
            lines = newLines

            # Iteración 
            for index, line in enumerate(lines):
                matches= re.search(regexPrimario, line)
                if ( matches ):
                    if (matches.group('com1') and matches.group('url1')) is not None:
                        comentario =  matches.group('com1')
                        if comentario.startswith('!'):
                            matchSecundario= re.search(regexSecundario, comentario)
                            if ( matchSecundario ):
                                if (matchSecundario.group('com1') and matchSecundario.group('url1')) is not None:
                                    comentario =  matchSecundario.group('com1')
                                    url        =  matchSecundario.group('url1')
                        else:
                            url = matches.group('url1')
                        antes=""
                        despues=""
                        if matches.group('pre') is not None:
                            antes=matches.group('pre') + " "
                        if matches.group('post') is not None:
                            despues=matches.group('post')
                        urlSplitted = url.rsplit('/', 1)
                        url = f'/assets/img/original/{urlSplitted[-1]:s}'
                        formato = '{: width="730px" padding:10px }'
                        lines[index] = "%s![%s](%s)%s%s" % (antes, comentario, url, formato, despues)
                        #print("!! ", lines[index])

        # Write back the file
        with open(pathFilenameOut, "w", encoding='utf-8') as fdOut:
            for line in lines:
                fdOut.write("%s\n" % line)


        #break
        continue
    else:
        continue


