const calculate = (n) => {
  let c = 0
  if (n === 0) return c = 0
  return c = Math.floor(calculate(n / 5) + n % 5)
}

const t = calculate()
console.log(t)

