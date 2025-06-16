Vue.createApp({
    data() {
        return {
            isSidebarCollapsed: true,
            staffNo: null,
            vehicleNo: null,
            startDate: '',
            endDate: '',
            speed: 30,
            violations: [],
            selectedEmployees: [],
            selectAll: false
        };
    },
    methods: {
        toggleSidebar() {
            this.isSidebarCollapsed = !this.isSidebarCollapsed;
        },
        async fetchViolations() {
            url=''
            if(this.staffNo==null && this.vehicleNo!=null){
                url=`/api/search_speed_violations/any/${this.vehicleNo}/${this.startDate}/${this.endDate}/${this.speed}/`
            }else if(this.vehicleNo==null && this.staffNo!=null){
                url=`/api/search_speed_violations/${this.staffNo}/any/${this.startDate}/${this.endDate}/${this.speed}/`
            }else if(this.staffNo==null && this.vehicleNo==null){
                url=`/api/search_speed_violations/any/any/${this.startDate}/${this.endDate}/${this.speed}/`
            }   
            try{
                const response = await fetch(url)
                if (!response.ok){
                    throw new Error(`Respose Status: ${response.status}`)
                }
            rawData = await response.json();
            this.violations = rawData.map(emp => ({ ...emp }));
            this.selectedEmployees = []; // reset selections
            this.selectAll = false;
            }catch(error){
                console.error(error.message)
            }
        },
        toggleSelectAll() {
            if (this.selectAll) {
            this.selectedEmployees = [...this.violations];
            } else {
            this.selectedEmployees = [];
            }
        },
        downloadExcel() {
            const wb = XLSX.utils.book_new();
            const wsData = [
                ["Staff No.", "Name", "Department", "Designation", "No. of Violations"],
                ...this.violations.map(emp => [
                emp.staffNo,
                emp.name,
                emp.department,
                emp.designation,
                ])
            ];

            const ws = XLSX.utils.aoa_to_sheet(wsData);
            XLSX.utils.book_append_sheet(wb, ws, "Violations");
            XLSX.writeFile(wb, "employee_violations.xlsx");
        }
    },
    mounted() {
        flatpickr(this.$refs.startDate, {
            dateFormat: "Y-m-d",
            onChange: ([selectedDate]) => {
              this.startDate = selectedDate.toISOString().split('T')[0]; // get only date
            }
          });
    
          flatpickr(this.$refs.endDate, {
            dateFormat: "Y-m-d",
            onChange: ([selectedDate]) => {
              this.endDate = selectedDate.toISOString().split('T')[0]; // get only date
            }
          });
        const urlParams = new URLSearchParams(window.location.search)
        this.staffNo = urlParams.get('staffNo')
        this.vehicleNo = urlParams.get('vehicleNo')
        this.startDate = urlParams.get('startDate')
        this.endDate = urlParams.get('endDate')
        this.speed = urlParams.get('speed')
        this.fetchViolations()
      },
      delimiters: ['[[', ']]']
}).mount("#app");
