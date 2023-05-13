for (let i = 0; i < 6; i++) {
    for (let j = 0; j < 6; j++) {
      if (first[i] === numbers[j]) {
        count += 1
        break
      }
    }
  }
  if (count === 6) {
    rank.innerText = '1등'
  }
  else if (count === 5) {
    for (let i = 0; i < 6; i++) {
      if (bonus === numbers[i]) {
        two_or_three = 2
        break
      }
    }
    if (two_or_three == 2) {
      rank.innerText = '2등'
    } 
    else {
      rank.innerText = '3등'
    }
  }
  else if (count === 4) {
    rank.innerText = '4등'
  }
  else if (count === 3) {
    rank.innerText = '5등'