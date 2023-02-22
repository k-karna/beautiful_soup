#This program is to find the HREF of the
# first <a> tag of a given HTML document

from bs4 import BeautifulSoup

html_doc = """

<!DOCTYPE HTML>
<html>

<head>
<title>Konark Karna - Git Page</title>
<meta charset="utf-8"/>
<meta name="author" content="Konark Karna">
<meta name="keywords" content="Konark Karna, Konark Karna India, Konark Karna Northumbria University, Konark Karna Newcastle, Konark Karna Computer Science,Data Scientist, Machine Learning Engineer, MSc Advanced Computer Science, Northumbria University,
			       Data Analysis, Data Visualization, Machine Learning, Neural Networks, Deep Learning, Natural Language Processing">
<link rel="stylesheet" type="text/css" href="basic.css">
<link href='http://fonts.googleapis.com/css?family=Play' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Exo+2:400' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=PT+Sans+Narrow' rel='stylesheet' type='text/css'>
</head>

<!--- Adding Google Analytics -->
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-154990580-2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-154990580-2');
</script>
<!-- End of Google Analytics Code -->

<body>
	<header>
		<h1><a href="https://k-karna.github.io/">GitLog</a></h1>
		<section id="nav">
			<ul>
				<li><a href="about.html">about</a></li>
				<li><a href="resume.html">resume</a></li>
				<li><a href="contact.html">contact</a></li>
				<li><a href="https://github.com/k-karna">github profile</a></li>
				<li><a href="http://www.konark.tumblr.com">weblog</a></li>
			</ul>	
		</section>
	</header>
	<section id="text">
		<p class="index">I'm just thrilled with the fact that programmers dealing with statistics are SCIENTISTS.</p> 
	</section>
	
</body>
</html>
"""
soup = BeautifulSoup(html_doc,'html.parser')

print("HREF of the first <a> tag:")
print(soup.find('a').attrs['href'])

print("HREF of the third <a> tag:")
print(soup.find_all('a')[2].attrs['href'])