clear
# 1. Directory Navigation - Naviger til Root folder
echo "Opgave 1:"
cd ~
echo "Navigeret til Root folder: $(pwd)\n"

# 2. Viewing Directory Contents - Udskriv fil og folder indhold i brugerens folder
echo "Opgave 2:"
echo "Indhold i Root folder:"
ls
echo "\n"

# 3. Creating files - Opret filen HelloWorld
echo "Opgave 3:"
touch HelloWorld
echo "HelloWorld fil oprettet."

# 4. Creating Directories - Opret folderen LinuxEmbedded
echo "\nOpgave 4:"
mkdir LinuxEmbedded
echo "Mappen LinuxEmbedded er oprettet.\n"

# 5. Copying Files - Kopier HelloWorld til LinuxEmbedded mappen
echo "Opgave 5:"
cp HelloWorld LinuxEmbedded/
echo "HelloWorld kopieret til LinuxEmbedded mappen."
echo "Indhold af LinuxEmbedded mappen:"
ls LinuxEmbedded/
echo "\n"

# 6. Renaming Files - Omdøb HelloWorld til Test i LinuxEmbedded
echo "Opgave 6:"
mv LinuxEmbedded/HelloWorld LinuxEmbedded/Test
echo "HelloWorld omdøbt til Test i LinuxEmbedded mappen."
echo "Indhold af LinuxEmbedded mappen efter omdøbning:"
ls LinuxEmbedded/
echo "\n"


# 7. Moving Files - Flyt HelloWorld fra home folder til LinuxEmbedded
echo "Opgave 7:"
mv HelloWorld LinuxEmbedded/
echo "HelloWorld flyttet til LinuxEmbedded mappen."
echo "Indhold af LinuxEmbedded mappen efter flytning:"
ls LinuxEmbedded/
echo "\n"

# 8. Deleting Files - Slet Test fil fra LinuxEmbedded
echo "Opgave 8:"
rm LinuxEmbedded/Test
echo "Test fil slettet fra LinuxEmbedded mappen."
echo "Indhold af LinuxEmbedded mappen efter sletning:"
ls LinuxEmbedded/
echo "\n"

# 9. Finding Files - Find placering af HelloWorld fil i filsystemet
echo "Opgave 9:"
echo "Søger efter HelloWorld fil:"
find ~ -name "HelloWorld"
echo "\n"

# 10. Write to file - Skriv 'Hello, World!' i filen HelloWorld
echo "Opgave 10:"
echo "Hello, World!" > LinuxEmbedded/HelloWorld
echo "Skrevet til filen HelloWorld."
echo "\n"

# 11. Displaying File Contents - Udskriv indhold af Test filen
echo "Opgave 11:"
echo "Indhold af HelloWorld fil:"
cat LinuxEmbedded/HelloWorld
echo "\n"