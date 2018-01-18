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
          <iu-toolbar color="grey lighten-4">
            <iu-button text="데이터 보기"
              @onEvent="confirm"></iu-button>
          </iu-toolbar>
        </v-flex>
      </v-layout>
    </v-container>
    <v-container>
      <v-layout>
        <v-flex xs12>
          <vue-c3 :handler="handler"></vue-c3>
        </v-flex>
      </v-layout>
    </v-container>
  </v-container>
</template>
 
<script>
import Vue from 'vue'
import VueC3 from 'vue-c3'

export default {
  components: {
    VueC3
  },
  props: ['options'],
  data() {
    return {
      handler: new Vue(),
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
  mounted() {
    this.handler.$emit('init', this.options)
  },
  watch: {
    'options.data': {
      handler(data) {
        this.handler.$emit('dispatch', chart => chart.load(data))
      }
    }
  },
  methods: {
    confirm() {
      console.log(this.startDate)
      console.log(this.startTime)
    }
  }
}
</script>