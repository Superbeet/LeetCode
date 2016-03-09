"""
public static IEnuerable<List<string>> ParseCSV(IEnumerable<char> S)
{
	if(string.IsNullOrEmpty(S))
		return null;

	List<string> line = new List<string>();
	StringbBuilder token = new StringBuilder();

	string prev = string.Empty;
	bool quote = false;
	foreach(char s in S)
	{
		if(s == '"')
		{

			// On the case of double quotes it will make this to true as previously
			// though that it was the closing quote previously making it false
			// So it quotes is false and it previously was a quote then this is a
			// double quote scenario
			if(quotes == false && prev == '"')
			{
				token.Append('"');
			}

			quotes = ~quotes;
		}

		if(quotes == true)
		{
			token.Append(s);
		}
		else if(s == ',')
		{
			line.Append(token.ToString());
			token.Clear();
		}
		else if(s == '\n')
		{
			line.Add(token.ToString());
			token.Clear();
			yield return line;

			line = new List<string>();
		}
		else
		{
			token.Append(s);
		}

		prev = s;
	}

	// Adding last item left
	line.Add(token.ToString());
	yield return line;
}
"""

# print csv_string

#e.g. input
# csv_string = "a, \"b, x\", c, \"q, p, r\", n, t"
# csv_string = "a,\"b\",c"
# csv_string = "a,\"b,x\",d"
csv_string = "a,\"b,x,\"\"\",d"
# csv_string = r'a,"b""","""""""c""","""d"""'
# csv_string = r'a,b,"""c""","""d"""'

def csv_parser(csv_str):
	if csv_str is "":
		return ""

	pre = ""

	elem = ""
	for x in csv_str.split('\n'):
	    inQuotes = False

	    for ch in x:

	        if ch not in ',"':
	            elem += ch

	        elif ch == '"':
	            inQuotes = not inQuotes

	        elif ch == ',':

	            if inQuotes:
	                elem += ch

	            else:
	                print elem
	                elem = ""  

	    print elem + "\n"

	    elem = ""

csv_parser(csv_string)

# def csv_parser(csv_str):
#     if csv_str is "":
#         return ""

#     line = []
#     elem = ""
#     prev = ""
#     for x in csv_str.split('\n'):
#         pre = ""
#         inQuotes = False

#         for ch in x:

#             if ch not in ',"':
#                 elem += ch

#             elif ch == '"':

#                 if inQuotes is False and prev == '"':
#                     elem += '"'

#                 inQuotes = not inQuotes

#             elif ch == ',':
#                 line.append(elem)
#                 elem = ""

#         prev = ch

#     return line