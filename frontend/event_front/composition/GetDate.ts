export const getDate = (monthFuture: number = 0) => {
  const date = new Date()
  // 日による桁上げの計算
  date.setMonth(date.getMonth() + monthFuture)
  const year = date.getFullYear()
  const month = ('00' + Number(date.getMonth() + 1)).slice(-2)
  const day = ('00' + date.getDate()).slice(-2)
  return `${year}-${month}-${day}`
}

export const getDateDay = (fullDate: string, future: number = 0) => {
  console.log('fullDate')
  console.log(fullDate)
  console.log('future')
  console.log(future)
  const date = new Date(fullDate)
  // 日による桁上げの計算
  date.setDate(date.getDate() + future)
  // date.setMonth(date.getMonth() + future)
  const year = date.getFullYear()
  const month = ('00' + Number(date.getMonth() + 1)).slice(-2)
  const day = ('00' + date.getDate()).slice(-2)
  console.log(`${year}-${month}-${day}`)
  return `${year}-${month}-${day}`
}
