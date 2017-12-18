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
    let childs = []

    for (let item of this.items) {
      let elements = []
      for (let member of item.group) {
        let element = null
        if (member.type === 'textfield') {
          element = this.createTextField(member)
        }
        elements.push(
          createElement(
            'v-flex',
            {
              class: {
                ...member.classes
              }
            },
            [element]
          )
        )
      }

      let element = createElement(
        'v-layout',
        {
          class: {
            row: true,
            wrap: true
          }
        },
        elements
      )

      if (item.expand) {
        childs.push(
          createElement(
            'iu-sub-header',
            {
              props: {
                text: item.expand
              }
            },
            [element]
          )
        )
      } else {
        childs.push(element)
      }
    }

    let form = createElement(
      'v-card',
      {
        props: {
          flat: true
        }
      },
      [
        createElement(
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
                ...childs,
                createElement('v-card-actions', {}, this.$slots.default)
              ]
            )
          ]
        )
      ]
    )

    return createElement(
      'v-layout',
      {
        class: {
          'justify-center': true
        }
      },
      [
        createElement(
          'v-flex',
          {
            class: {
              xs12: true,
              sm10: true,
              md8: true,
              lg6: true
            }
          },
          [form]
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
    }
  }
}
</script>