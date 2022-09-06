#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  list.map(
    (elem) => {
      if (elem === searchElement) {
        num += 1;
        return 1;
      } else {
        return 0;
      }
    }
  );
  return num;
};
