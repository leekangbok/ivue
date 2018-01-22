<template>
  <v-dialog v-model="dialog"
    persistent
    max-width="400px">
    <v-btn small
      outline
      @click.native="onLogout"
      slot="activator">{{ status ? '로그아웃' : '로그인' }}
    </v-btn>
    <v-card>
      <v-card-text>
        <v-container grid-list-md>
          <v-layout wrap>
            <v-flex xs12>
              <v-text-field label="아이디"
                required></v-text-field>
            </v-flex>
            <v-flex xs12>
              <v-text-field label="패스워드"
                type="password"
                required></v-text-field>
            </v-flex>
          </v-layout>
        </v-container>
        <small>*필수입력</small>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary"
          @click.native="dialog = false">취소</v-btn>
        <v-btn color="primary"
          @click.native="onLogin">로그인</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import types from '@/store/mutation-types'

export default {
  data() {
    return {
      dialog: false
    }
  },
  computed: {
    status: {
      get() {
        return this.$store.state[types.LOGIN_STATUS]
      },
      set(value) {
        this.$store.commit(types.LOGIN_STATUS, value)
      }
    }
  },
  methods: {
    onLogin() {
      this.dialog = false
      this.status = !this.status
    },
    onLogout(event) {
      if (this.status) {
        event.stopPropagation()
        this.status = !this.status
      }
    }
  }
}
</script>
