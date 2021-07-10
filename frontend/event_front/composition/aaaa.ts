import { SendForms } from '@/types/interfaces'
import {
  computed,
  isRef,
  Ref,
  InjectionKey,
  reactive,
  toRef,
  toRefs
} from '@nuxtjs/composition-api'

type baseState = {
  response: string[]
  error: Error | null
  isLoading: boolean
}
export const UseGlobalState = () => {
  let globalState = reactive<SendForms>({
    keyword: [],
    address: [],
    limit: 0,
    start_from: '',
    start_to: '',
    target: []
  })
  const SetSendForm = (stateValue: SendForms) => {
    globalState = stateValue
  }

  return {
    ...toRefs(globalState),
    SetSendForm
  }
}
type GlobalStateType = ReturnType<typeof UseGlobalState>
export const GlobalStateKey: InjectionKey<GlobalStateType> = Symbol(
  'GlobalState'
)
