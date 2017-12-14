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
                createElement('v-card-actions', {}, this.$slots.default)
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
    }
  }
}
</script>