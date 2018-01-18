<template>
  <v-container>
    <v-container grid-list-lg>
      <v-layout row
        wrap>
        <v-flex xs12
          sm6>
          <v-menu lazy
            :close-on-content-click="false"
            v-model="menu"
            transition="scale-transition"
            offset-y
            full-width
            :nudge-right="40"
            max-width="290px"
            min-width="290px">
            <v-text-field slot="activator"
              label="시작 날짜"
              v-model="startDate"
              prepend-icon="event"
              readonly></v-text-field>
            <v-date-picker v-model="startDate"
              no-title
              scrollable
              actions>
              <template slot-scope="{ save, cancel }">
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn flat
                    color="primary"
                    @click="cancel">취소</v-btn>
                  <v-btn flat
                    color="primary"
                    @click="save">확인</v-btn>
                </v-card-actions>
              </template>
            </v-date-picker>
          </v-menu>
        </v-flex>
        <v-flex xs12
          sm6>
          <v-menu lazy
            :close-on-content-click="false"
            v-model="menu2"
            transition="scale-transition"
            offset-y
            full-width
            :nudge-right="40"
            max-width="290px"
            min-width="290px">
            <v-text-field slot="activator"
              label="시작 시각"
              v-model="startTime"
              prepend-icon="access_time"
              readonly></v-text-field>
            <v-time-picker v-model="startTime"
              actions>
              <template slot-scope="{ save, cancel }">
                <v-card-actions>
                  <v-btn flat
                    color="primary"
                    @click="cancel">취소</v-btn>
                  <v-btn flat
                    color="primary"
                    @click="save">확인</v-btn>
                </v-card-actions>
              </template>
            </v-time-picker>
          </v-menu>
        </v-flex>
        <v-flex xs12
          sm6>
          <v-menu lazy
            :close-on-content-click="false"
            v-model="modal"
            transition="scale-transition"
            offset-y
            full-width
            :nudge-right="40"
            max-width="290px"
            min-width="290px">
            <v-text-field slot="activator"
              label="종료 날짜"
              v-model="endDate"
              prepend-icon="event"
              readonly></v-text-field>
            <v-date-picker v-model="endDate"
              no-title
              scrollable
              actions>
              <template slot-scope="{ save, cancel }">
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn flat
                    color="primary"
                    @click="cancel">취소</v-btn>
                  <v-btn flat
                    color="primary"
                    @click="save">확인</v-btn>
                </v-card-actions>
              </template>
            </v-date-picker>
          </v-menu>
        </v-flex>
        <v-flex xs12
          sm6>
          <v-menu lazy
            :close-on-content-click="false"
            v-model="modal2"
            transition="scale-transition"
            offset-y
            full-width
            :nudge-right="40"
            max-width="290px"
            min-width="290px">
            <v-text-field slot="activator"
              label="종료 시각"
              v-model="endTime"
              prepend-icon="access_time"
              readonly></v-text-field>
            <v-time-picker v-model="endTime"
              actions>
              <template slot-scope="{ save, cancel }">
                <v-card-actions>
                  <v-btn flat
                    color="primary"
                    @click="cancel">취소</v-btn>
                  <v-btn flat
                    color="primary"
                    @click="save">확인</v-btn>
                </v-card-actions>
              </template>
            </v-time-picker>
          </v-menu>
        </v-flex>
        <v-flex xs12>
          <iu-toolbar>
            <iu-button text="확인"
              icon="refresh"
              @onEvent="confirm"></iu-button>
          </iu-toolbar>
        </v-flex>
      </v-layout>
    </v-container>
    <v-container>
      <v-layout>
        <v-flex xs12>
          <iu-c3 :options="options"></iu-c3>
        </v-flex>
      </v-layout>
    </v-container>
  </v-container>
</template>

<script>
import Types from '@/store/mutation-types'
import { mapActions, mapGetters } from 'vuex'

export default {
  data() {
    return {
      startDate: null,
      endDate: null,
      menu: false,
      modal: false,
      startTime: null,
      endTime: null,
      menu2: false,
      modal2: false
    }
  },
  computed: {
    ...mapGetters({
      options: Types.GET_BITCOIN_RECENT_TRANSACTIONS
    })
  },
  methods: {
    confirm() {
      this.getOptions({
        startDate: this.startDate,
        endDate: this.endDate,
        startTime: this.startTime,
        endTime: this.endTime,
        type: 'BTC'
      }).then(response => console.log(response))
    },
    // getRandomInt(min, max) {
    //   return Math.floor(Math.random() * (max - min)) + min
    // },
    ...mapActions({
      getOptions: Types.GET_BITCOIN_RECENT_TRANSACTIONS
    })
  },
  mounted() {}
}
</script>

