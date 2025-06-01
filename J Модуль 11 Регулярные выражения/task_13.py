regex = r'<!--.*?-->'

# input() => Hi, your tags <!-bee-> and <--geek--> are incorrect. Correct tags look like <!--beegeek-->
# output() => <!--beegeek-->

# input() => <!-- header of page --> <-- incorrect header of page !-->
# output() => <!-- header of page -->