export const getDate = (futer: number = 0) => {
  const date = new Date()
  // 月による桁上げの計算
  date.setMonth(date.getMonth() + futer)
  const year = date.getFullYear()
  const month = ('00' + Number(date.getMonth() + 1)).slice(-2)
  const day = ('00' + date.getDate()).slice(-2)
  return `${year}-${month}-${day}`
}
