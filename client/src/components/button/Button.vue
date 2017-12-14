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
    iconOnly: Boolean
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
        props: {
          disabled: !this.valid,
          color: 'primary',
          small: true,
          icon: this.iconOnly
        },
        on: {
          click: this.onClick
        }
      },
      children
    )
  },
  methods: {
    onClick() {
      this.$emit(this.targetEvent)
    }
  }
}
</script>