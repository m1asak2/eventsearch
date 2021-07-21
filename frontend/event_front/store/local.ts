import { DisplayForm, SendForms, SaveForm, EventData } from '@/types/interfaces'
import { toRefs, reactive } from '@nuxtjs/composition-api'
import { SaveToDisplayForm } from '~/composition/ConvertForm'

export const state: SaveForm = {
  keyword: 'string',
  address: 'string',
  limit: 0,
  period: 'string',
  target: []
}
type localState = {
  saveData: SaveForm[]
}
export default () => {
  const key = 'eventData'
  const abb = reactive({
    localdata: [] as SaveForm[]
  })
  const state = reactive<localState>({
    saveData: []
  })
  const load = (): SaveForm[] => {
    if (key in localStorage) {
      const tmp = localStorage.getItem('eventData') || ''
      return JSON.parse(tmp)
    }
    return []
  }
  const save = (data: SaveForm): SaveForm[] => {
    const savedata = load()
    savedata.push(data)
    localStorage.setItem(key, JSON.stringify(savedata))
    return savedata
  }
  const remove = (index: number): SaveForm[] => {
    const savedata = load()
    savedata.splice(index, 1)
    localStorage.setItem(key, JSON.stringify(savedata))
    return savedata
  }
  return {
    ...toRefs(state),
    save,
    load,
    remove
  }
}
