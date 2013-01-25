function syllabify(word){
  var alphabet = $('#alphabet').text().split();
  var vowelRE = '([aeiou]+)';
  var alphabetRE = '(' + alphabet.join('|') + ')';
  //return $.trim(word).split(new RegExp(alphabetRE));
  return $.trim(word).split(new RegExp(vowelRE));
  
}
