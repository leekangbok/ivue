<script>
export default {
  props: {
    text: {
      type: String,
      default: ''
    },
    valid: {
      type: Boolean,
      default: true
    },
    targetEvent: {
      type: String,
      default: 'onEvent'
    },
    icon: Boolean,
    iconOnly: Boolean,
    outline: Boolean,
    color: {
      type: String,
      default: 'primary'
    },
    classes: {
      type: Object,
      default() {
        return {}
      }
    },
    flat: Boolean
  },
  render(createElement) {
    let children = []

    if (this.icon) {
      children = [
        createElement(
          'v-icon',
          {
            class: {
              'ma-0': true,
              'pa-0': true
            },
            props: {
              light: true,
              left: true
            }
          },
          [this.text]
        )
      ]
    } else {
      children = [this.text]
    }

    return createElement(
      'v-btn',
      {
        class: this.classes,
        props: {
          flat: this.flat,
          disabled: !this.valid,
          color: this.color,
          small: true,
          outline: this.outline,
          icon: this.iconOnly
        },
        on: {
          click: () => this.$emit(this.targetEvent)
        }
      },
      children
    )
  }
}
</script>