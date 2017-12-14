<script>
export default {
  props: {
    items: Array,
    fluid: Boolean
  },
  data() {
    return {
      valid: false
    }
  },
  render(createElement) {
    let children = []

    for (let item of this.items) {
      for (let member of item.members) {
        let element = null
        if (member.type === 'textfield') {
          element = this.createTextField(member)
        }
        children.push(
          createElement(
            'v-flex',
            {
              class: {
                xs12: true,
                [`sm${12 / item.members.length}`]: true
              }
            },
            [element]
          )
        )
      }
    }

    // v-layout을 sub-header로 묶어야함.
    // children = [
    //   createElement(
    //     'iu-sub-header',
    //     {
    //       props: {
    //         text: '펼치기'
    //       }
    //     },
    //     children
    //   )
    // ]

    return createElement(
      'v-form',
      {
        props: {
          value: this.valid
        }
      },
      [
        createElement(
          'v-container',
          {
            class: {
              fluid: this.fluid,
              'grid-list-lg': true
            }
          },
          [
            createElement(
              'v-card',
              {
                props: {
                  flat: true
                }
              },
              [
                createElement(
                  'v-layout',
                  {
                    class: {
                      row: true,
                      wrap: true
                    }
                  },
                  children
                ),
                // createElement('iu-sub-header', {}, [createElement(
                //   'v-layout',
                //   {
                //     class: {
                //       row: true,
                //       wrap: true
                //     }
                //   },
                //   children
                // )]),
                createElement('v-card-actions', {}, [
                  createElement('small', {}, ['*는 필수 입력입니다.']),
                  createElement('v-spacer', {}),
                  createElement('iu-button', {
                    props: {
                      text: '저장'
                    },
                    on: {
                      onEvent: this.onSave
                    }
                  })
                ])
              ]
            )
          ]
        )
      ]
    )
  },
  methods: {
    createTextField(item) {
      return this.$createElement('v-text-field', {
        props: {
          label: item.label,
          required: item.required,
          value: item.model
        },
        on: {
          input(value) {
            item.model = value
          }
        }
      })
    },
    onSave() {
      console.log('save')
      this.$emit('onSave')
    }
  }
}
</script>